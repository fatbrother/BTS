// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import "./ConcertTicketNFT.sol";

contract ConcertTickets {
    string public eventName;
    address public issuer;
    uint256 public eventId;
    uint256 public totalTickets;
    uint256 public reservationStart;
    uint256 public reservationEnd;
    address[] public reservations;
    address[] public whitelists;
    mapping(address => bool) public winners;
    mapping(uint256 => address) public ticketOwners;
    ConcertTicketNFT public nftContract;

    constructor(
        string memory _eventName,
        uint256 _totalTickets,
        uint256 _reservationStart,
        uint256 _reservationEnd,
        address[] memory _whitelists,
        address _nftContract
    ) {
        require(_totalTickets > 0, "Total tickets must be greater than zero");
        require(_reservationStart < _reservationEnd, "Invalid time range");
        require(totalTickets == 0, "Event details already set");

        eventId = uint256(keccak256(abi.encodePacked(_eventName, block.timestamp)));
        eventName = _eventName;
        issuer = msg.sender;
        totalTickets = _totalTickets;
        reservationStart = _reservationStart;
        reservationEnd = _reservationEnd;
        whitelists = _whitelists;
        nftContract = ConcertTicketNFT(_nftContract);
    }

    modifier onlyIssuer() {
        require(msg.sender == issuer, "Only issuer can call this function");
        _;
    }

    modifier onlyWhitelisted() {
        require(msg.sender == issuer || isWhitelisted(msg.sender), "Not whitelisted");
        _;
    }

    function isWhitelisted(address _address) public view returns (bool) {
        for (uint256 i = 0; i < whitelists.length; i++) {
            if (whitelists[i] == _address) {
                return true;
            }
        }
        return false;
    }

    function reserveTicket() external onlyWhitelisted {
        require(
            block.timestamp >= reservationStart,
            "Reservation period not started"
        );
        require(block.timestamp <= reservationEnd, "Reservation period ended");
        for (uint256 i = 0; i < reservations.length; i++) {
            require(reservations[i] != msg.sender, "Already reserved");
        }

        reservations.push(msg.sender);
    }

    function endReservation() external onlyIssuer {
        reservationEnd = block.timestamp;
    }

    function selectWinners(uint256 randomSeed) external onlyIssuer {
        require(block.timestamp > reservationEnd, "Reservation period not ended");
        require(reservations.length > 0, "No reservations");
        require(totalTickets > 0, "No tickets to distribute");

        uint256 numWinners = (totalTickets >= reservations.length)
            ? reservations.length
            : totalTickets;

        if (totalTickets >= reservations.length) {
            for (uint256 i = 0; i < reservations.length; i++) {
                address winnerAddress = reservations[i];
                winners[winnerAddress] = true;
                ticketOwners[i + 1] = winnerAddress;
            }
        } else {
            uint256[] memory indices = new uint256[](reservations.length);
            for (uint256 i = 0; i < reservations.length; i++) {
                indices[i] = i;
            }

            for (uint256 i = 0; i < indices.length; i++) {
                uint256 j = uint256(
                    keccak256(abi.encodePacked(randomSeed, i))
                ) % indices.length;
                (indices[i], indices[j]) = (indices[j], indices[i]);
            }

            for (uint256 i = 0; i < numWinners; i++) {
                address winnerAddress = reservations[indices[i]];
                winners[winnerAddress] = true;
                ticketOwners[i + 1] = winnerAddress;
            }
        }
    }

    function mintTicket() external {
        require(winners[msg.sender], "Not a winner");
        winners[msg.sender] = false;
        nftContract.mint(msg.sender, eventId);
    }
}
