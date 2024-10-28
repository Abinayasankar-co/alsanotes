
import './AuthPage.css';


const LoginPage = () => {
  return (
    <div className="auth-container">
      <div className="glass-card">
        {/* Logo Section */}
        <div className="logo-section">
          <img src="/logo.png" alt="Logo" className="logo" />
          <a href="#" className="back-to-website">Back to website</a>
        </div>

        {/* Title Section */}
        <div className="title-section">
          <h2>Login</h2>
          <p>Don't have an account? <a href="/signup">Create an account</a></p>
        </div>

        {/* Form Section */}
        <div className="form-section">
          <form>
            <input type="email" className="form-control mt-3" placeholder="Email" required />
            <input type="password" className="form-control mt-3" placeholder="Enter your password" required />
          </form>
        </div>

        {/* Submit Button */}
        <div className="button-section">
          <button type="submit" className="btn btn-primary btn-block">Login</button>
        </div>

        {/* Social Login Section */}
        <div className="social-login-section">
          <p>Or login with</p>
          <div className="social-buttons">
            <button className="btn btn-outline-dark">
              <i className="fab fa-google"></i> Google
            </button>
            <button className="btn btn-outline-dark">
              <i className="fab fa-apple"></i> Apple
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
