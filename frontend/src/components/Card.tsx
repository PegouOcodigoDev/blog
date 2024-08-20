import { ReactNode } from "react"

type Props = {
    children?: ReactNode
}

export default ({children}:Props) => {

    return (
        <div className="card">
            {children}
        </div>
    )
}