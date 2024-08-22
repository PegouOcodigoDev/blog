type Props = {
    label: string;
    password?: boolean
    onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
    value: string;
}

export default ({label, password, onChange, value}: Props) =>{
    return (
<label
  htmlFor={label}
  className="peer relative block rounded-md border border-black shadow-sm focus-within:border-blue-600 focus-within:ring-1 focus-within:ring-blue-600"
>
  <input
    type={password ? "password": "text" }
    id={label}
    className="peer text-sm p-1.5 bg-transparent placeholder-transparent focus:border-transparent focus:outline-none focus:ring-0"
    placeholder={label}
    onChange={onChange}
    value={value}
  />

  <span
    className="pointer-events-none absolute start-2.5 top-0 -translate-y-3/4 text-xs text-gray-700 transition-all peer-placeholder-shown:top-1/2 peer-placeholder-shown:text-sm peer-focus:top-0 peer-focus:text-md"
  >
    {label}
  </span>
</label>
    )
}