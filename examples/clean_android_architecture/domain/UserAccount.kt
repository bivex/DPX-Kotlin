package com.example.cleanandroid.domain

import kotlinx.serialization.Serializable

@JvmInline
value class UserId(val value: String)

@Serializable
data class UserAccount(
    val id: UserId,
    val username: String,
    val email: String,
    val balance: Double = 0.0
)

sealed interface UserUiState {
    object Loading : UserUiState
    data class Success(val user: UserAccount) : UserUiState
    data class Error(val message: String) : UserUiState
}
