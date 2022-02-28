pragma solidity ^0.4.14;

contract Test {
    uint[2] a;
    function test() returns(uint, uint) {
        a[0] = 1;
        a[1] = 2;
        
        return (a[0], a[1]);
    }
}