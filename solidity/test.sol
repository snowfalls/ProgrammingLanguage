pragma solidity ^0.4.14;

contract Test {
    uint a;
    
    function func1() external {
        
    }
    
    function func2() {
        this.func1();
    }
}

contract owned {
    address owner;
    
    function owned() {
        owner = msg.sender;
    }
}

contract Parent is owned {
    uint x;
    function Parent(uint _x) {
        x = _x;
    }
    
    function parentFunc1() internal {
        if (msg.sneder == owner) self
    }
}