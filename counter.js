let counter = 0;
function count() {
    counter++;
    document.querySelector("h1").innerHTML = counter;
    if (counter % 10 === 0) {
        alert(`Count is now ${counter}`);
    } else {
        document.querySelector("h1").style.color = "red";
    }
}
// Attach the count function to the button click event
// This will ensure that the function is called when the button is clicked
document.addEventListener("DOMContentLoaded", function () {
    document.querySelector("button").onclick = count;
});