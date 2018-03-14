Rails.application.routes.draw do
  get 'welcome/index'
  get "welcome/positions", to: "welcome#positions", as: :positions  
  get "welcome/pokedex", to: "welcome#pokedex", as: :pokedex  

  root 'welcome#index'


  devise_for :users
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
