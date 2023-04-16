import React, { Component } from "react"
import { render } from "react-dom"
import {
    BrowserRouter as Router,
    Routes,
    Route,
} from "react-router-dom";

import { Test1 } from "./Test1";
import { Test2 } from "./Test2";

export default class App extends Component {
   constructor(props) {
       super(props);
   }

//    render() {
//        return <h1>Hello I'm Maaaaaaaaakkori.</h1>;
//    }

    render() {
        return (
            < div className="app">
                <Router>
                    <Routes>
                        <Route path="/" element={<Test1 />} />
                        <Route path="/result" element={<Test2/>} />
                    </Routes>
                </Router>
            </ div>
        );
    }

}

const appDiv = document.getElementById("app");
render(<App/>, appDiv)