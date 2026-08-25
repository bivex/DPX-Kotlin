package com.example.cleanandroid.presentation

import androidx.compose.runtime.Composable
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import com.example.cleanandroid.domain.UserAccount

@Composable
fun UserProfileScreen(user: UserAccount) {
    val isExpanded = remember { mutableStateOf(false) }
    UserCardView(user = user)
}

@Composable
fun UserCardView(user: UserAccount) {
    Text(text = user.username)
}
