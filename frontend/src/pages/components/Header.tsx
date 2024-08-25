import { useSelector } from "react-redux";
import { handleGetAccessToken } from "../../utils/auth";
import { RootState } from "../../redux/store";
import SearchBar from "./SearchBar";

export const Header = () => {
  const isLogged = handleGetAccessToken();
  const user = useSelector((state: RootState) => state.auth.user);

  return (
    <header className="bg-white">
      <div className="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div className="flex h-16 items-center justify-between">
          <div className="md:flex md:items-center md:gap-12">
            <a className="block text-teal-600" href="#">
              <span className="sr-only">Home</span>
              <img className="size-28" src="../../../public/assets/logo.png" alt="Logo" />
            </a>
          </div>
          <div className="hidden md:block">
            <nav aria-label="Global">
              <SearchBar />
            </nav>
          </div>

          {!isLogged ? (
            <div className="flex items-center gap-4">
              <div className="sm:flex sm:gap-4">
                <a
                  className="rounded-md bg-emerald-500 px-5 py-2.5 text-sm font-medium text-white shadow"
                  href="/login"
                >
                  logar
                </a>

                <div className="hidden sm:flex">
                  <a
                    className="rounded-md bg-gray-100 px-5 py-2.5 text-sm font-medium text-emerald-500"
                    href="/signup"
                  >
                    Registrar-se
                  </a>
                </div>
              </div>
            </div>
          ) : (
            <div className="flex flex-row items-center">
              <strong className="text-black text-sm text-end m-4 font-serif font-light">
                Bem vindo novamente, {user?.name}
              </strong>
              <div className="size-14 rounded-full border-black border ">
                <img alt="Avatar" className="rounded-full" />
              </div>
            </div>
          )}
        </div>
      </div>
    </header>
  );
};