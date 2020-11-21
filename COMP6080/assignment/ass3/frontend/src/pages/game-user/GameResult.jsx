import React from 'react';
import { useParams } from 'react-router-dom'
import { BarChart, CartesianGrid, XAxis, YAxis, Tooltip, Legend, Bar } from "recharts";

const GameResult = () => {
    const { playerId, right, wrong } = useParams()
    const data = [
        {
            'name': `playerID: ${playerId}`,
            'right': right,
            'wrong': wrong
        }
    ]

    return (
        <div style={{ margin: '10%', fontSize: '20px' }}>
            <BarChart width={1000} height={400} data={data}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="right" fill="#8884d8" />
                <Bar dataKey="wrong" fill="#82ca9d" />
            </BarChart>
        </div>
    );
};

export default GameResult;