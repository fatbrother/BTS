// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract ConcertTickets {
    address public issuer;
    uint256 public totalTickets;
    uint256 public reservationStart;
    uint256 public reservationEnd;
    address[] public reservations;
    mapping(address => bool) public reservationMap;
    mapping(address => uint256) public winners;
    mapping(uint256 => address) public ticketOwners;

    constructor() {
        issuer = msg.sender;
    }

    modifier onlyIssuer() {
        require(msg.sender == issuer, "Only issuer can call this function");
        _;
    }

    function setEventDetails(
        uint256 _totalTickets,
        uint256 _reservationStart,
        uint256 _reservationEnd
    ) external onlyIssuer {
        require(_totalTickets > 0, "Total tickets must be greater than zero");
        require(_reservationStart < _reservationEnd, "Invalid time range");
        require(totalTickets == 0, "Event details already set");

        totalTickets = _totalTickets;
        reservationStart = _reservationStart;
        reservationEnd = _reservationEnd;
    }

    function reserveTicket() external {
        require(
            block.timestamp >= reservationStart,
            "Reservation period not started"
        );
        require(block.timestamp <= reservationEnd, "Reservation period ended");
        require(!reservationMap[msg.sender], "Already reserved");

        reservations.push(msg.sender);
        reservationMap[msg.sender] = true;
    }

    function getReservations() external view returns (address[] memory) {
        return reservations;
    }

    function endReservation() public onlyIssuer {
        reservationEnd = block.timestamp;
    }

    function selectWinners(uint256 randomSeed) public onlyIssuer {
        require(block.timestamp > reservationEnd, "Reservation period not ended");
        require(reservations.length > 0, "No reservations");
        require(totalTickets > 0, "No tickets to distribute");

        uint256 numWinners = (totalTickets >= reservations.length)
            ? reservations.length
            : totalTickets;

        if (totalTickets >= reservations.length) {
            for (uint256 i = 0; i < reservations.length; i++) {
                address winnerAddress = reservations[i];
                winners[winnerAddress] = i + 1;
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
                winners[winnerAddress] = i + 1;
                ticketOwners[i + 1] = winnerAddress;
            }
        }
    }
}
