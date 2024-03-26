import React from "react";

function HelloWorldButton(){
    const handleClick = () =>{
        alert("Hello World");
    };

    return (
        <button onClick={handleClick}>Click Me</button>
    );
}

export default HelloWorldButton;