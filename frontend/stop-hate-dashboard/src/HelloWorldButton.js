import React from "react";

function HelloWorldButton(){
    const handleClick = () =>{
        alert("Hello World");
    };

    return (
        <button onClick={handleClick}>Oh, not today! Not even second to code. Apparently, i had 60 second to add this :)</button>
    );
}

export default HelloWorldButton;