import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        axios.get('/api/data')
            .then(response => {
                setData(response.data);
                setLoading(false);
            })
            .catch(error => {
                console.error("حدث خطأ أثناء جلب البيانات:", error);
            });
    }, []);

    if (loading) {
        return <p>جاري تحميل البيانات...</p>;
    }

    return (
        <div>
            <h1>لوحة معلومات التداول</h1>
            <table>
                <thead>
                    <tr>
                        <th>الرمز</th>
                        <th>السعر</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map((item, index) => (
                        <tr key={index}>
                            <td>{item.symbol}</td>
                            <td>{item.price}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default App;
