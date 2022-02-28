pragma solidity ^0.4.14;

contract Payroll {
    
    struct Employee {
        address id;
        uint salary;
        uint lastPayday;
    }
    
    uint constant payDuration = 10 seconds;
    uint  totalSalary;
    address owner;
    mapping(address => Employee) public employees;
    
    function Payroll() {
        owner = msg.sender;
    }
    
    function _partialPaid(Employee employee) private {
        uint payment = employee.salary * (now - employee.lastPayday) / payDuration;
        employee.id.transfer(payment);
    }
    
    function addEmployee(address employeeId, uint salary) {
        require(msg.sender == owner);  
        var employee = employees[employeeId];
        assert(employee.id == 0x0);
        employees[employeeId] = Employee(employeeId, salary * 1 ether, now);
        totalSalary += employees[employeeId].salary;
    }
    
    function removeEmployee(address employeeId) {
        require(msg.sender == owner);
        
        var employee = employees[employeeId];
        assert(employee.id !=  0x0);
        _partialPaid(employee);
        totalSalary -= employees[employeeId].salary;
        delete employees[employeeId];
        // employees[employeeId] = employees[employees.length - 1];
        // employees.length -= 1;
        return;

    }
    
    function updateEmployee(address employeeId, uint salary) {
        require(msg.sender == owner);

        var employee = employees[employeeId];
        assert(employee.id !=  0x0);
        _partialPaid(employee);
        totalSalary -= employees[employeeId].salary;
        employees[employeeId].salary = salary * 1 ether;
        totalSalary += employees[employeeId].salary;
        employees[employeeId].lastPayday = now;
    }
    
    function addFund() payable returns (uint) {
        return this.balance;
    }
    
    function calculateRunway() returns (uint) {
        return this.balance / totalSalary;
    }
    
    function hasEnoughFund() returns (bool) {
        return calculateRunway() > 0;
    }
    
    function checkEmployee(address employeeId) returns(uint salary, uint lastPayday) {
        var employee = employees[employeeId];
        salary = employee.salary;
        lastPayday = employee.lastPayday;
        // return (employee.salary, employee.lastPayday);
    }
    
    function getPaid() {
        var employee = employees[msg.sender];
        assert(nextPayDay < now);
        uint nextPayDay = employee.lastPayday + payDuration;
        assert(nextPayDay < now);
          
        employees[msg.sender].lastPayday = nextPayDay;
        employee.id.transfer(employee.salary);
    }
}

