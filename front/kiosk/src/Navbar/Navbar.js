import React from 'react';
import { Link } from "react-router-dom";
import styles from './Navbar.module.css';
import logo from '../assets/logo.png';

function App() {
  return (
      <nav className={styles.wrapper}>
          <img src={logo} />
          <div className={styles.menu}>
              <Link to='/Main' style={{textDecoration: "none"}}>
                  <span className={styles.main}>버거</span>
              </Link>
              <Link to='/Beverage' style={{textDecoration: "none"}}>
                  <span className={styles.beverage}>음료</span>
              </Link>
              <Link to='/Sidemenu' style={{textDecoration: "none"}}>
                  <span className={styles.sidemenu}>사이드 메뉴</span>
              </Link>
          </div>
      </nav>
  );
}

export default App;
