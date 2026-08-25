package com.example.cleanandroid.data

object NetworkConfig {
    const val BASE_URL = "https://api.example.com/v1"
    const val TIMEOUT_SECONDS = 30L

    class ClientFactory private constructor() {
        companion object {
            fun createClient(): NetworkClient {
                return NetworkClient(BASE_URL)
            }
        }
    }
}

class NetworkClient(val endpoint: String)
