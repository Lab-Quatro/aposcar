import React from "react";
import AposcarLogo from "../../assets/icons/AposcarLogo";
import Button from "../Button";
import { useRouter } from "next/router";
import Link from "next/link";
import useAuth from "../../utils/useAuth";
import { LogoutIcon } from "@heroicons/react/outline";
import ProfileButton from "./ProfileButton";

const Navbar: React.FC = () => {
  const router = useRouter();
  const { loggedUser, logout } = useAuth();

  return (
    <nav className="px-10 py-3 flex justify-between items-center flex-none">
      <Link href="/">
        <a>
          <AposcarLogo />
        </a>
      </Link>
      <div>
        {loggedUser ? (
          <div className="flex items-center space-x-4">
            <button onClick={logout} title="Logout">
              <LogoutIcon className="text-white w-7 h-7 rotate-180" />
            </button>
            <ProfileButton user={loggedUser} />
          </div>
        ) : (
          <Button color="primary" onClick={() => router.push("/register")}>
            Register
          </Button>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
