import React from 'react';
import Link from 'next/link';

function Header() {
    return (
        <header>
            <div className="container">
                <div className="navbar">
                    <div className="logo">
                        <Link href="/">SCIENTIA</Link>
                    </div>
                    <div className="textItem">
                        <Link href="/publications">Пcубликации</Link>
                        <Link href="/authors">Авторы</Link>
                        <Link href="/about">О проекте</Link>
                    </div>
                    <div className="login">
                        <button type="button" className="SignIn">Войти</button>
                    </div>
                </div>
            </div>
        </header>
    );
}

export default Header;
