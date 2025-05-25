// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";

contract ConcertTicketNFT is ERC721, Ownable, ERC721Burnable {
    uint256 public nextTokenId;
    address public ticketingContract;
    address public validator; // 驗票合約或地址

    struct TicketInfo {
        uint256 eventId;
    }

    mapping(uint256 => TicketInfo) public tickets;

    constructor() ERC721("Concert Ticket", "CTKT") Ownable(msg.sender) {}

    function setTicketingContract(address _ticketingContract) external onlyOwner {
        ticketingContract = _ticketingContract;
    }

    function setValidator(address _validator) external onlyOwner {
        validator = _validator;
    }

    modifier onlyTicketing() {
        require(msg.sender == ticketingContract, "Not ticketing contract");
        _;
    }

    modifier onlyValidator() {
        require(msg.sender == validator, "Not validator");
        _;
    }

    function mint(address to, uint256 eventId) external onlyTicketing {
        uint256 tokenId = nextTokenId++;
        _safeMint(to, tokenId);
        tickets[tokenId] = TicketInfo(eventId);
    }

    function validateEntry(uint256 tokenId, uint256 eventId) external view onlyValidator {
        require(ownerOf(tokenId) != address(0), "Invalid token");
        require(tickets[tokenId].eventId == eventId, "Event mismatch");
    }

    function getTicketInfo(uint256 tokenId) external view returns (uint256) {
        TicketInfo memory t = tickets[tokenId];
        return (t.eventId);
    }

    function burnTicket(uint256 tokenId) external onlyTicketing {
        require(ownerOf(tokenId) != address(0), "Invalid token");
        _burn(tokenId);
        delete tickets[tokenId];
    }
}
