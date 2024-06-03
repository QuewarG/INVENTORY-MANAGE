import { useContext, useEffect, useRef } from "react";
import { ThemeContext } from "../../context/ThemeContext";
import { LIGHT_THEME } from "../../constants/themeConstants";
import LogoBlue from "../../assets/images/logo_blue.svg";
import LogoWhite from "../../assets/images/logo_white.svg";
import { 
    MdOutlineAttachMoney,
    MdOutlineBarChart,
    MdOutlineClose,
    MdNewspaper,
    MdOutlineCurrencyExchange,
    MdOutlineGridView,
    MdOutlineLogout,
    MdOutlineMessage,
    MdOutlinePeople,
    MdOutlineSettings,
    MdOutlineShoppingBag,
    MdBorderColor,
    MdBarChart,
    MdMenu  } from "react-icons/md";
import { Link } from "react-router-dom";
import "./Sidebar.scss";
import { SidebarContext, SidebarProvider } from "../../context/SidebarContext";


const Sidebar = () => {
    const {theme} = useContext(ThemeContext);
    const {isSidebarOpen, closeSidebar} = useContext(SidebarContext);
    const navbarRef = useRef(null);

    // closing the navbar when clicked outside the sidebar area
    const handleClickOutside = (event) => {
        if(navbarRef.current && !navbarRef.current.contains(event.target) && event.target.className != "sidebar-open-btn"){
            closeSidebar();
        }
    }

    useEffect(() => {
        document.addEventListener("mousedown", handleClickOutside);
        return () => {
            document.removeEventListener("mousedown", handleClickOutside)
        };
    }, []);
    
    return (
        <nav className={`sidebar ${isSidebarOpen ? "sidebar-show" : ""}`} 
        ref={navbarRef}
        >
            <div className="sidebar-top">
                <div className="sidebar-brand">
                    <img src={theme == LIGHT_THEME ? LogoBlue : LogoWhite} alt="" />
                    <span className="sidebar-brand-text">
                        App
                    </span>
                </div>
                <button className="sidebar-close-btn" onClick={closeSidebar}>
                <MdOutlineClose size={24}/>
                </button>
            </div>
            <div className="sidebar-body">
                <div className="sidebar-menu">
                    <ul className="menu-list">
                        <li className="menu-item">
                            <Link to = "/dashboard" className="menu-link active">
                                <span className="menu-link-icon">
                                    <MdOutlineGridView size={16}/>
                                </span>
                                <span className="menu-link-text"> Dashboard </span>
                            </Link>
                        </li>
                        <li className="menu-item">
                            <Link to = "/quotes" className="menu-link">
                                <span className="menu-link-icon">
                                    <MdNewspaper size={20}/>
                                </span>
                                <span className="menu-link-text"> Quotes </span>
                            </Link>
                        </li>
                        <li className="menu-item">
                            <Link to = "/sales" className="menu-link">
                                <span className="menu-link-icon">
                                    <MdOutlineAttachMoney size={20}/>
                                </span>
                                <span className="menu-link-text"> Sales </span>
                            </Link>
                        </li>
                        <li className="menu-item">
                            <Link to = "/products" className="menu-link">
                                <span className="menu-link-icon">
                                    <MdOutlineShoppingBag size={20}/>
                                </span>
                                <span className="menu-link-text"> Products</span>
                            </Link>
                        </li>
                        <li className="menu-item">
                            <Link to = "/orders" className="menu-link">
                                <span className="menu-link-icon">
                                    <MdBorderColor size={20}/>
                                </span>
                                <span className="menu-link-text"> Orders</span>
                            </Link>
                        </li>
                        <li className="menu-item">
                            <Link to = "/users" className="menu-link">
                                <span className="menu-link-icon">
                                    <MdOutlinePeople size={20}/>
                                </span>
                                <span className="menu-link-text"> Users </span>
                            </Link>
                        </li>
                    </ul>
                </div>

                <div className="sidebar-menu sidebar-menu2">
                    <ul className="menu-list">
                        <li className="menu-item">
                            <Link to = "/" className="menu-link">
                                <span className="menu-link-icon">
                                    <MdOutlineSettings size={20}/>
                                </span>
                                <span className="menu-link-text"> Settings </span>
                            </Link>
                        </li>
                        <li className="menu-item">
                            <Link to = "/" className="menu-link">
                                <span className="menu-link-icon">
                                    <MdOutlineLogout size={20}/>
                                </span>
                                <span className="menu-link-text"> LogOut </span>
                            </Link>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    )
}

export default Sidebar