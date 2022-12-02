import React from "react";
import logo from "../img/logo.svg";
import './admin_Navbar.css';

function Admin_nav(){
    return(
        <>
        <div className="navbar">
            <img src={logo}></img>
        </div>
        </>
    );
}
export default Admin_nav;