package com.example.cleanandroid.domain

import kotlinx.coroutines.flow.Flow

interface UserRepository {
    suspend fun getUser(id: UserId): UserAccount?
    suspend fun saveUser(user: UserAccount)
    fun observeUsers(): Flow<List<UserAccount>>
}
