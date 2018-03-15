class AddimglinkToPokemons < ActiveRecord::Migration[5.1]
  def change
  	add_column :pokemons, :imagelink, :string
  end
end
