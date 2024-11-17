
function navigate(){
    window.location = "/login";
}


const Navbar = () => (
    <nav className="bg-gray-800 p-4 fixed w-full top-0 z-10">
        <div className="container mx-auto flex justify-between items-center">
            <div className="flex column ">
            <div className="text-white text-lg font-bold">ALSA NOTES</div>
            <div className="text-white text-lg font-bold">Contact</div>
            </div>
            <div>
                <button className="bg-yellow-500 text-gray-900 px-4 py-2 rounded" type="button" id="login" >Login</button>
            </div>
        </div>
    </nav>
);

export default Navbar;