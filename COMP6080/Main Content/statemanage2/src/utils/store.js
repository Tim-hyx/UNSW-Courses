import React from 'react'

export const StoreContext = React.createContext(null)

export default ({ children }) => {
  const [movies, setMovies] = React.useState([])
  const [tvShows, setTvShows] = React.useState([])

  const store = {
    movies: [movies, setMovies],
    tvShows: [tvShows, setTvShows],
  }

  return <StoreContext.Provider value={store}>{children}</StoreContext.Provider>
}