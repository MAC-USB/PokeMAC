Rails.application.routes.draw do
  get 'welcome/index'
  get "welcome/positions", to: "welcome#positions", as: :positions  
  get "pokedex/quest", to: "pokedex#quest", as: :pokedex 
  get "pokedex/pokemon", to: "pokedex#pokemons", as: :pokemons

  root 'welcome#index'

  resources :questions
  devise_for :users
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
