import React, { useState, useEffect } from 'react';
import { Route, Routes, Link } from "react-router-dom";
import axios from 'axios';
import { Card, Row, Col } from "antd";
import Navbar from "../Navbar/Navbar";
import styles from './Main.module.css';

function App() {
    const [Products, setProducts] = useState([])

    useEffect(() => {
        getProduct();
    }, [])

    const getProduct = (event) => {
        axios.get("") // request������, 8���� �����ֶ�� body�� ���� ����
        .then(function(response){
            // setProducts(response.data);
        }).catch(function(event){
            // alert("��ǰ����� �������µ� �����߽��ϴ�.");
        })
    }

    const renderCards = Products.map((product, index) => {
        return <Col key={index}> 
            <Card className={styles.card}
                // cover = {Products.length > 6 ? <img src={Products.slice(0,6)}/> : <img src={product.files}/>} //������ �������� �̹��� ����
                // title={product.Title}
                // description={product.Description} // ������ 
            >
            </Card>
        </Col>
    })

    return (
        <div>
            <div className={styles.mainbox}>
                <Navbar />
            </div>
            
            <Row>
                {renderCards}  
            </Row>

            <div className={styles.bottombox2}>
                <span className={styles.total}>�� ���� �ݾ�</span>
                <span className={styles.account}>x,xxx��</span>
            </div>
            <div className={styles.bottombox1}>
                <Link to=''>
                    <span className={styles.calbtn}>�����ϱ�</span>
                </Link>
            </div>
        </div>
    );
}

export default App;
