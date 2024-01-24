const max = prompt("Enter the max number: ");
console.log(max);

const random = Math.floor(Math.random() * max) + 1;
console.log(random);

let guess = prompt("Guess the number: ");
while(true) {
    if(guess == "quit") {
        console.log("User quite");
        break;
    }

    if(guess == random) {
        console.log("Congratulations! You are right, random number was: ",random);
        break;
    } else if(guess < random){
        guess = prompt("Sorry, Your guess was too small. Try again......");
    } else {
        guess = prompt("Sorry, Your guess was too large. Try again......");
    }
}