package com.example.cleanandroid.data

import com.example.cleanandroid.domain.UserAccount
import com.example.cleanandroid.domain.UserId
import com.example.cleanandroid.domain.UserRepository
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.withContext

class UserRepositoryImpl : UserRepository {
    private val _usersFlow = MutableStateFlow<List<UserAccount>>(emptyList())

    override suspend fun getUser(id: UserId): UserAccount? = withContext(Dispatchers.IO) {
        _usersFlow.value.find { it.id == id }
    }

    override suspend fun saveUser(user: UserAccount) = withContext(Dispatchers.IO) {
        val updated = _usersFlow.value.toMutableList().apply {
            removeAll { it.id == user.id }
            add(user)
        }
        _usersFlow.value = updated
    }

    override fun observeUsers(): Flow<List<UserAccount>> = _usersFlow.asStateFlow()
}
