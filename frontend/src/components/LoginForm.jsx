// src/components/LoginForm.jsx
import { useState } from "react";
import { loginUser, getCurrentUser } from "../api";

export default function LoginForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [user, setUser] = useState(null);

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      await loginUser({ email, password });
      const me = await getCurrentUser();
      setUser(me);
    } catch (err) {
      alert("Login failed: " + err.message);
    }
  };

  return (
    <div>
      {user ? (
        <p>Welcome {user.full_name}!</p>
      ) : (
        <form onSubmit={handleLogin}>
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <button type="submit">Login</button>
        </form>
      )}
    </div>
  );
}
