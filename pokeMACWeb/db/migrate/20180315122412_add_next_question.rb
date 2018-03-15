class AddNextQuestion < ActiveRecord::Migration[5.1]
  def change
  	add_column :questions, :question, :reference
  end
end
