#include<stdio.h>


int main(){
do {
    turn=scanf("Enter the value of turn")
    while(turn != 0); // Wait until turn is 0
    
    // Critical section
    // Code for the critical section goes here

    turn = 1; // Set turn to allow the other process to enter
    
    // Remainder section
    // Code for the remainder section goes here
} while (1);
}