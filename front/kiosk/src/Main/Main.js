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
        axios.get("") // request보낼때, 8개만 보내주라고 body랑 같이 보냄
        .then(function(response){
            // setProducts(response.data);
        }).catch(function(event){
            // alert("상품목록을 가져오는데 실패했습니다.");
        })
    }

    const renderCards = Products.map((product, index) => {
        return <Col key={index}> 
            <Card className={styles.card}
                // cover = {Products.length > 6 ? <img src={Products.slice(0,6)}/> : <img src={product.files}/>} //가져온 데이터의 이미지 띄우기
                // title={product.Title}
                // description={product.Description} // 상세정보 
            >
            </Card>
        </Col>
    })

    return (
        <div>
            <Navbar />
            
            {/* <Row>
                {renderCards}  
            </Row> */}

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
