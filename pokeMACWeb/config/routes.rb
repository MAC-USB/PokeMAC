Rails.application.routes.draw do
  get 'welcome/index', to: "welcome#index", as: :welcome
  get "welcome/positions", to: "welcome#positions", as: :positions  
  get "pokedex/quest", to: "pokedex#quest", as: :pokedex
  get "pokedex/quest/:id", to: "pokedex#show", as: :questions
  get "pokedex/pokelist", to: "pokedex#pokelist", as: :pokelist
  get "pokedex/pokemon/:id", to: "pokedex#pokemons", as: :pokemons

  root 'welcome#comienza'

  resources :questions
  devise_for :users
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
