// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {

    uint256 favoriteNumber;

    // uint256 favoriteNumber = 5;
    // bool favoriteBool = false;
    // string favString = "String";
    // int256 favInt = -5;
    // address favaddr = 0x5D7541f344DD45ad2116e969219a6Aa38bf1003D;
    // bytes32 favBytes = "cat";


    // This is a comment!
    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People[] public people;
    mapping(string => uint256) public nameToFavoriteNumber;

    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
        // store(5);
    } 

    // function retrieve() public view{
    //     favoriteNumber+favoriteNumber;
    // }
    

    function retrieve() public view returns (uint256){
        return favoriteNumber;
    }
    // till this

    // memory will delete the variable after exe
    //storage will not delete
    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People(_favoriteNumber, _name));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}