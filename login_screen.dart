import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:job4job/screens/auth/register_screen.dart';
import 'package:job4job/screens/candidate/home_screen.dart';
import 'package:job4job/screens/recruiter/recruiter_home_screen.dart';
import 'package:job4job/widgets/bottom_nav_bar.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> with TickerProviderStateMixin {
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  bool isLoading = false;
  bool isObscure = true;
  String? selectedRole;

  late AnimationController _fadeController;
  late AnimationController _slideController;
  late Animation<double> _fadeAnimation;
  late Animation<Offset> _slideAnimation;

  @override
  void initState() {
    super.initState();

    // Animation setup
    _fadeController = AnimationController(
      duration: const Duration(milliseconds: 1200),
      vsync: this,
    );
    _slideController = AnimationController(
      duration: const Duration(milliseconds: 800),
      vsync: this,
    );

    _fadeAnimation = Tween<double>(begin: 0.0, end: 1.0).animate(
      CurvedAnimation(parent: _fadeController, curve: Curves.easeOut),
    );

    _slideAnimation = Tween<Offset>(
      begin: const Offset(0, 0.3),
      end: Offset.zero,
    ).animate(CurvedAnimation(parent: _slideController, curve: Curves.easeOutCubic));

    _fadeController.forward();
    _slideController.forward();
  }

  @override
  void dispose() {
    _fadeController.dispose();
    _slideController.dispose();
    emailController.dispose();
    passwordController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
            colors: [
              const Color(0xFF6C63FF),
              const Color(0xFF4834DF),
              const Color(0xFF2D1B69),
            ],
          ),
        ),
        child: SafeArea(
          child: SingleChildScrollView(
            physics: const BouncingScrollPhysics(),
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 24),
              child: FadeTransition(
                opacity: _fadeAnimation,
                child: SlideTransition(
                  position: _slideAnimation,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const SizedBox(height: 40),

                      // ===== Logo & Brand =====
                      _buildHeader(),

                      const SizedBox(height: 50),

                      // ===== Login Card =====
                      Container(
                        decoration: BoxDecoration(
                          color: Colors.white,
                          borderRadius: BorderRadius.circular(30),
                          boxShadow: [
                            BoxShadow(
                              color: Colors.black.withOpacity(0.15),
                              blurRadius: 30,
                              offset: const Offset(0, 10),
                            ),
                          ],
                        ),
                        child: Padding(
                          padding: const EdgeInsets.all(28),
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              // Title
                              Text(
                                "Đăng nhập",
                                style: GoogleFonts.poppins(
                                  fontSize: 28,
                                  fontWeight: FontWeight.bold,
                                  color: const Color(0xFF2D1B69),
                                ),
                              ),
                              const SizedBox(height: 8),
                              Text(
                                "Khám phá cơ hội nghề nghiệp tuyệt vời",
                                style: GoogleFonts.poppins(
                                  fontSize: 14,
                                  color: Colors.grey[600],
                                ),
                              ),

                              const SizedBox(height: 30),

                              // Email Field
                              _buildModernTextField(
                                controller: emailController,
                                hint: "Email của bạn",
                                icon: Icons.email_outlined,
                              ),

                              const SizedBox(height: 20),

                              // Password Field
                              _buildModernTextField(
                                controller: passwordController,
                                hint: "Mật khẩu",
                                icon: Icons.lock_outline,
                                obscureText: isObscure,
                                suffix: IconButton(
                                  icon: Icon(
                                    isObscure ? Icons.visibility_off_outlined : Icons.visibility_outlined,
                                    color: const Color(0xFF6C63FF),
                                    size: 22,
                                  ),
                                  onPressed: () {
                                    setState(() => isObscure = !isObscure);
                                  },
                                ),
                              ),

                              const SizedBox(height: 16),

                              // Forgot Password
                              Align(
                                alignment: Alignment.centerRight,
                                child: TextButton(
                                  onPressed: () {
                                    // Handle forgot password
                                  },
                                  child: Text(
                                    "Quên mật khẩu?",
                                    style: GoogleFonts.poppins(
                                      color: const Color(0xFF6C63FF),
                                      fontWeight: FontWeight.w600,
                                      fontSize: 13,
                                    ),
                                  ),
                                ),
                              ),

                              const SizedBox(height: 20),

                              // Role Selection
                              _buildRoleSelection(),

                              const SizedBox(height: 30),

                              // Login Button
                              _buildLoginButton(),

                              const SizedBox(height: 24),

                              // Divider
                              Row(
                                children: [
                                  Expanded(child: Divider(color: Colors.grey[300], thickness: 1)),
                                  Padding(
                                    padding: const EdgeInsets.symmetric(horizontal: 16),
                                    child: Text(
                                      "hoặc",
                                      style: GoogleFonts.poppins(
                                        color: Colors.grey[500],
                                        fontSize: 13,
                                      ),
                                    ),
                                  ),
                                  Expanded(child: Divider(color: Colors.grey[300], thickness: 1)),
                                ],
                              ),

                              const SizedBox(height: 24),

                              // Social Login
                              _buildSocialLogin(),
                            ],
                          ),
                        ),
                      ),

                      const SizedBox(height: 30),

                      // Register Link
                      _buildRegisterLink(),

                      const SizedBox(height: 40),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }

  // ===== Header with Logo =====
  Widget _buildHeader() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Container(
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(
            color: Colors.white.withOpacity(0.2),
            borderRadius: BorderRadius.circular(16),
          ),
          child: Icon(
            Icons.work_outline_rounded,
            color: Colors.white,
            size: 32,
          ),
        ),
        const SizedBox(height: 16),
        Text(
          "Job4Job",
          style: GoogleFonts.poppins(
            fontSize: 36,
            fontWeight: FontWeight.bold,
            color: Colors.white,
            letterSpacing: -1,
          ),
        ),
        Text(
          "Nơi kết nối nhân tài",
          style: GoogleFonts.poppins(
            fontSize: 16,
            color: Colors.white.withOpacity(0.9),
            fontWeight: FontWeight.w300,
          ),
        ),
      ],
    );
  }

  // ===== Modern Text Field =====
  Widget _buildModernTextField({
    required TextEditingController controller,
    required String hint,
    required IconData icon,
    bool obscureText = false,
    Widget? suffix,
  }) {
    return Container(
      decoration: BoxDecoration(
        color: Colors.grey[50],
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.grey[200]!, width: 1.5),
      ),
      child: TextField(
        controller: controller,
        obscureText: obscureText,
        style: GoogleFonts.poppins(
          fontSize: 15,
          color: const Color(0xFF2D1B69),
        ),
        decoration: InputDecoration(
          prefixIcon: Container(
            margin: const EdgeInsets.all(12),
            padding: const EdgeInsets.all(8),
            decoration: BoxDecoration(
              color: const Color(0xFF6C63FF).withOpacity(0.1),
              borderRadius: BorderRadius.circular(10),
            ),
            child: Icon(icon, color: const Color(0xFF6C63FF), size: 20),
          ),
          suffixIcon: suffix,
          hintText: hint,
          hintStyle: GoogleFonts.poppins(
            color: Colors.grey[400],
            fontSize: 14,
          ),
          border: InputBorder.none,
          contentPadding: const EdgeInsets.symmetric(horizontal: 20, vertical: 18),
        ),
      ),
    );
  }

  // ===== Role Selection =====
  Widget _buildRoleSelection() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          "Bạn đang tìm kiếm với vai trò",
          style: GoogleFonts.poppins(
            fontSize: 15,
            fontWeight: FontWeight.w600,
            color: const Color(0xFF2D1B69),
          ),
        ),
        const SizedBox(height: 12),
        Row(
          children: [
            _buildRoleCard(
              role: "Ứng viên",
              icon: Icons.person_search_outlined,
              gradient: const LinearGradient(
                colors: [Color(0xFF6C63FF), Color(0xFF5A52D5)],
              ),
            ),
            const SizedBox(width: 12),
            _buildRoleCard(
              role: "Nhà tuyển dụng",
              icon: Icons.business_center_outlined,
              gradient: const LinearGradient(
                colors: [Color(0xFFFF6B9D), Color(0xFFC44569)],
              ),
            ),
          ],
        ),
      ],
    );
  }

  Widget _buildRoleCard({
    required String role,
    required IconData icon,
    required Gradient gradient,
  }) {
    final bool isSelected = selectedRole == role;

    return Expanded(
      child: GestureDetector(
        onTap: () {
          setState(() => selectedRole = role);
        },
        child: AnimatedContainer(
          duration: const Duration(milliseconds: 300),
          curve: Curves.easeInOut,
          padding: const EdgeInsets.symmetric(vertical: 16),
          decoration: BoxDecoration(
            gradient: isSelected ? gradient : null,
            color: isSelected ? null : Colors.grey[100],
            borderRadius: BorderRadius.circular(16),
            border: Border.all(
              color: isSelected ? Colors.transparent : Colors.grey[300]!,
              width: 1.5,
            ),
            boxShadow: isSelected
                ? [
                    BoxShadow(
                      color: (role == "Ứng viên"
                          ? const Color(0xFF6C63FF)
                          : const Color(0xFFFF6B9D)).withOpacity(0.4),
                      blurRadius: 15,
                      offset: const Offset(0, 6),
                    ),
                  ]
                : [],
          ),
          child: Column(
            children: [
              Icon(
                icon,
                color: isSelected ? Colors.white : Colors.grey[600],
                size: 32,
              ),
              const SizedBox(height: 8),
              Text(
                role,
                textAlign: TextAlign.center,
                style: GoogleFonts.poppins(
                  color: isSelected ? Colors.white : Colors.grey[700],
                  fontWeight: isSelected ? FontWeight.bold : FontWeight.w500,
                  fontSize: 13,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  // ===== Login Button =====
  Widget _buildLoginButton() {
    return Container(
      decoration: BoxDecoration(
        gradient: const LinearGradient(
          colors: [Color(0xFF6C63FF), Color(0xFF4834DF)],
        ),
        borderRadius: BorderRadius.circular(16),
        boxShadow: [
          BoxShadow(
            color: const Color(0xFF6C63FF).withOpacity(0.4),
            blurRadius: 20,
            offset: const Offset(0, 8),
          ),
        ],
      ),
      child: ElevatedButton(
        onPressed: isLoading ? null : _handleLogin,
        style: ElevatedButton.styleFrom(
          backgroundColor: Colors.transparent,
          shadowColor: Colors.transparent,
          minimumSize: const Size(double.infinity, 58),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(16),
          ),
        ),
        child: isLoading
            ? const SizedBox(
                height: 24,
                width: 24,
                child: CircularProgressIndicator(
                  color: Colors.white,
                  strokeWidth: 2.5,
                ),
              )
            : Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text(
                    "Đăng nhập",
                    style: GoogleFonts.poppins(
                      color: Colors.white,
                      fontWeight: FontWeight.bold,
                      fontSize: 16,
                    ),
                  ),
                  const SizedBox(width: 8),
                  const Icon(Icons.arrow_forward_rounded, color: Colors.white, size: 20),
                ],
              ),
      ),
    );
  }

  // ===== Social Login =====
  Widget _buildSocialLogin() {
    return Row(
      children: [
        _buildSocialButton(
          icon: Icons.g_mobiledata_rounded,
          label: "Google",
          onTap: () {
            // Handle Google login
          },
        ),
        const SizedBox(width: 12),
        _buildSocialButton(
          icon: Icons.facebook_rounded,
          label: "Facebook",
          onTap: () {
            // Handle Facebook login
          },
        ),
      ],
    );
  }

  Widget _buildSocialButton({
    required IconData icon,
    required String label,
    required VoidCallback onTap,
  }) {
    return Expanded(
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(14),
        child: Container(
          padding: const EdgeInsets.symmetric(vertical: 14),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(14),
            border: Border.all(color: Colors.grey[300]!, width: 1.5),
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(icon, color: Colors.grey[700], size: 24),
              const SizedBox(width: 8),
              Text(
                label,
                style: GoogleFonts.poppins(
                  color: Colors.grey[700],
                  fontWeight: FontWeight.w600,
                  fontSize: 14,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  // ===== Register Link =====
  Widget _buildRegisterLink() {
    return Center(
      child: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text(
            "Chưa có tài khoản?",
            style: GoogleFonts.poppins(
              color: Colors.white.withOpacity(0.9),
              fontSize: 14,
            ),
          ),
          TextButton(
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (_) => const RegisterScreen()),
              );
            },
            child: Text(
              "Đăng ký ngay",
              style: GoogleFonts.poppins(
                color: Colors.white,
                fontWeight: FontWeight.bold,
                fontSize: 14,
                decoration: TextDecoration.underline,
                decorationColor: Colors.white,
              ),
            ),
          ),
        ],
      ),
    );
  }

  // ===== Handle Login =====
  Future<void> _handleLogin() async {
    if (selectedRole == null) {
      _showErrorSnackBar("Vui lòng chọn vai trò trước khi đăng nhập");
      return;
    }

    if (emailController.text.isEmpty || passwordController.text.isEmpty) {
      _showErrorSnackBar("Vui lòng điền đầy đủ thông tin");
      return;
    }

    setState(() => isLoading = true);
    await Future.delayed(const Duration(seconds: 2));

    if (!mounted) return;

    // Navigate based on role
    if (selectedRole == "Ứng viên") {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (_) => const MainNavigation()),
      );
    } else if (selectedRole == "Nhà tuyển dụng") {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (_) => const RecruiterHomeScreen()),
      );
    }

    setState(() => isLoading = false);
  }

  void _showErrorSnackBar(String message) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Row(
          children: [
            const Icon(Icons.error_outline, color: Colors.white),
            const SizedBox(width: 12),
            Expanded(
              child: Text(
                message,
                style: GoogleFonts.poppins(
                  color: Colors.white,
                  fontWeight: FontWeight.w500,
                ),
              ),
            ),
          ],
        ),
        backgroundColor: const Color(0xFFFF6B9D),
        behavior: SnackBarBehavior.floating,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
        margin: const EdgeInsets.all(16),
      ),
    );
  }
}
