import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        pinterest: {
          red: '#E60023',
          'red-hover': '#AD081B',
          dark: '#111111',
          gray: '#767676',
          'light-gray': '#E9E9E9',
        },
      },
    },
  },
  plugins: [],
}
export default config
