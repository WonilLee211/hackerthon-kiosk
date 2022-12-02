import React from 'react';
import { Link } from "react-router-dom";
import styles from './Navbar.module.css';

function App() {
  return (
      <nav className={styles.wrapper}>
          <div>
              <Link to='/Main'>
                  <span className={styles.main}></span>
              </Link>
              <Link to='/Burger'>
                  <span className={styles.burger}></span>
              </Link>
              <Link to='/Beverage'>
                  <span className={styles.beverage}></span>
              </Link>
              <Link to='/Sidemenu'>
                  <span className={styles.sidemenu}></span>
              </Link>
          </div>
      </nav>
  );
}

export default App;
