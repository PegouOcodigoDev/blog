type Props = {
    label: string;
    onClick?: () => void
}

export default ({label, onClick}: Props) =>{
    return (
        <button className="btn-primary" onClick={onClick}>
            {label}
        </button>
    )
}