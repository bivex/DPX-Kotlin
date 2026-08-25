package com.example.cleanandroid.presentation

import com.example.cleanandroid.domain.UserId
import com.example.cleanandroid.domain.UserRepository
import com.example.cleanandroid.domain.UserUiState
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

class UserViewModel(
    private val repository: UserRepository,
    private val scope: CoroutineScope
) {
    private val _uiState = MutableStateFlow<UserUiState>(UserUiState.Loading)
    val uiState: StateFlow<UserUiState> = _uiState.asStateFlow()

    fun loadUser(id: UserId) {
        scope.launch {
            _uiState.value = UserUiState.Loading
            val user = repository.getUser(id)
            if (user != null) {
                _uiState.value = UserUiState.Success(user)
            } else {
                _uiState.value = UserUiState.Error("User not found")
            }
        }
    }
}
