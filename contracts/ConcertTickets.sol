// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract ConcertTickets {
    address public issuer;
    uint256 public totalTickets;
    uint256 public reservationStart;
    uint256 public reservationEnd;
    bool public reservationEnded;

    address[] public reservations;
    mapping(address => bool) public reservationMap;

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
}
