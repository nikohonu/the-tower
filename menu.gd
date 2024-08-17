extends Control


func _ready() -> void:
	pass


func _notification(what):
	if what == NOTIFICATION_WM_CLOSE_REQUEST:
		get_tree().quit()


func _on_play_pressed() -> void:
	get_tree().change_scene_to_file("res://level1.tscn")


func _on_exit_pressed() -> void:
	get_tree().root.propagate_notification(NOTIFICATION_WM_CLOSE_REQUEST)
