import { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../../context/AuthContext";

function Login() {

    const navigate = useNavigate();

    const { login } = useContext(AuthContext);

    const [username, setUsername] = useState("");

    const [password, setPassword] = useState("");

    const [error, setError] = useState("");

    const handleSubmit = async (e) => {

        e.preventDefault();

        setError("");

        const result = await login(username, password);

        if (result.success) {

            navigate("/dashboard");

        }

        else {

            setError("Invalid Username or Password");

        }

    };

    return (

        <div className="container">

            <div className="login-card card shadow p-4">

                <h2 className="text-center mb-4">

                    Student Management System

                </h2>

                <form onSubmit={handleSubmit}>

                    <div className="mb-3">

                        <label className="form-label">

                            Username

                        </label>

                        <input

                            type="text"

                            className="form-control"

                            value={username}

                            onChange={(e) =>
                                setUsername(e.target.value)
                            }

                            required

                        />

                    </div>

                    <div className="mb-3">

                        <label className="form-label">

                            Password

                        </label>

                        <input

                            type="password"

                            className="form-control"

                            value={password}

                            onChange={(e) =>
                                setPassword(e.target.value)
                            }

                            required

                        />

                    </div>

                    {

                        error &&

                        <div className="alert alert-danger">

                            {error}

                        </div>

                    }

                    <button

                        className="btn btn-primary w-100"

                    >

                        Login

                    </button>

                </form>

            </div>

        </div>

    );

}

export default Login;