import React from "react";
import logo from "../img/logo.svg";
import './admin_Navbar.css';

function Admin_nav(){
    return(
        <>
        <div className="navbar">
            <img src={logo}></img>
        </div>
        
        <div className="label">
            <div>주문번호</div>
            <div>주문내역</div>
            <div>주문수량</div>
            <div>총 내용</div>
        </div>
        </>
    )
}
export default Admin_nav;