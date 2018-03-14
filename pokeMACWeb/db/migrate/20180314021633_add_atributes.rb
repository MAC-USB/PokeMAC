class AddAtributes < ActiveRecord::Migration[5.1]
  def change
  	add_column :users, :questions, :boolean, array: true
  end
end
