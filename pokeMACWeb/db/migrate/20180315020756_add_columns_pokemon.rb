class AddColumnsPokemon < ActiveRecord::Migration[5.1]
  def change
  	add_column :pokemons, :name, :string
  	add_column :pokemons, :habilities, :string
  end
end
