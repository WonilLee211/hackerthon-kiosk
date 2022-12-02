import React from 'react';
import { Link } from "react-router-dom";
import styles from './Navbar.module.css';

function App() {
  return (
      <nav className={styles.wrapper}>
          <div className={styles.menu}>
              <Link to='/Main' className={styles.main}>
                  <span>버거</span>
              </Link>
              <Link to='/Beverage' className={styles.beverage}>
                  <span>음료</span>
              </Link>
              <Link to='/Sidemenu' className={styles.sidemenu}>
                  <span>사이드 메뉴</span>
              </Link>
          </div>
      </nav>
  );
}

export default App;
