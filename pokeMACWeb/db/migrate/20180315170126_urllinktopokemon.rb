class Urllinktopokemon < ActiveRecord::Migration[5.1]
  def change
  	add_column :pokemons, :image, :string
  end
end
