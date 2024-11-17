const LoginPage = () => (
    <div className="flex items-center justify-center min-h-screen bg-gray-900">
        <div className="bg-gray-800 p-8 rounded-lg shadow-lg w-full max-w-md">
            <h2 className="text-3xl font-bold text-yellow-500 mb-6">Sign In</h2>
            <form className="space-y-4">
                <div>
                    <label className="block text-lg font-medium text-gray-300">Email</label>
                    <input type="email" className="w-full p-2 border border-gray-700 rounded bg-gray-700 text-gray-300" />
                </div>
                <div>
                    <label className="block text-lg font-medium text-gray-300">Password</label>
                    <input type="password" className="w-full p-2 border border-gray-700 rounded bg-gray-700 text-gray-300" />
                </div>
                <button type="submit" className="w-full bg-yellow-500 text-gray-900 px-4 py-2 rounded">Sign In</button>
            </form>
        </div>
    </div>
);

export default LoginPage;