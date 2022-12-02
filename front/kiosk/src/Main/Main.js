import React, { useState, useEffect } from 'react';
import { Route, Routes, Link } from "react-router-dom";
import axios from 'axios';
import { Card, Row, Col } from "antd";
import Navbar from "../Navbar/Navbar";
import styles from './Main.module.css';
import qrcode from '../assets/qrcode.png';

function App() {
    const [Products, setProducts] = useState([])

    useEffect(() => {
        getProduct();
    }, [])

    const getProduct = (event) => {
        axios.get("http://127.0.0.1:8000/api/v1/beverages/") // request보낼때, 8개만 보내주라고 body랑 같이 보냄
        .then(function (response) {
            setProducts(response.data);
        }).catch(function (event) {
            console.log(event)
            alert("상품목록을 가져오는데 실패했습니다.");
        })
    }

    const renderCards = Products.map((product, index) => {
        console.log('http://localhost:8000/' + product.image)
        return <Col key={index}> 
            <Card className={styles.card}
                cover={<img src={'http://127.0.0.1:8000/' + product.image} />} //가져온 데이터의 이미지 띄우기
                title={product.Title}
                description={product.Description} // 상세정보 
            >
            </Card>
        </Col>
    })

    return (
        <div>
            <Navbar />
            
            <Row>
                {renderCards}  
            </Row>

            <div className={styles.qrbox}>
                <img src={qrcode} /> <br />
                <span>빠른 결제를 위해</span> <br />
                <span>Easy Kiosk를 사용해 보세요</span> <br />
                <span>1. Easy Kiosk를 연다</span> <br />
                <span>2. QR 코드를 찍는다</span> <br />
                <span>3. 주문을 한다</span> <br />
                <span>4. 제품을 수령한다</span>
            </div>
            <div className={styles.bottombox2}>
                <span className={styles.total}>총 결제 금액</span>
                <span className={styles.account}>x,xxx원</span>
            </div>
            <div className={styles.bottombox1}>
                <Link to=''>
                    <span className={styles.calbtn}>결제하기</span>
                </Link>
            </div>
        </div>
    );
}

export default App;
