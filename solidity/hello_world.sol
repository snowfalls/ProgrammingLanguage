pragma solidity ^0.4.21;

contract SimpleStorage{
    uint storedData;
    
    function set(uint x) {
        storedData = x;
    }
    
    function get() view returns(uint){
        storedData = 1;
        return storedData;
    }
}